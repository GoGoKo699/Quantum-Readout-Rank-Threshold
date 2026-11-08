"""Deterministic Laplace-integral checks for continuous-Haar pair information.

The exact expectations are defined in science/haar-pair-readout.md. This checks
normalization, moment factors and representative values; it is neither a finite
Clifford simulation nor the proof of the eventual strict inequality.
"""
import json
from pathlib import Path
import mpmath as mp

mp.mp.dps = 35

def check(e):
    e = mp.mpf(e)
    L = 1-e
    q = L*e
    p = [L*L,L*e,e*e]
    breaks=[mp.mpf(0),mp.mpf(1),1/e,1/(e*e),mp.inf]
    def integ(extra):
        def f(t):
            denominators=[1+t*x for x in p]
            v=mp.mpf(1)
            for a in denominators:
                v/=a
            for i in extra:
                v/=denominators[i]
            return v
        return mp.quad(f,breaks)
    g=[integ([i]) for i in range(3)]
    h={(i,j):integ([i,j]) for i in range(3) for j in range(i,3)}
    residuals=[abs(sum(p[i]*g[i] for i in range(3))-1)]
    for j in range(3):
        residuals.append(abs(sum(p[i]*h[min(i,j),max(i,j)]*(2 if i==j else 1) for i in range(3))-1))
    moment_residual=max(residuals)
    if moment_residual > mp.mpf("1e-25"):
        raise AssertionError(f"Laplace normalization or second moment: {moment_residual}")
    # Diagonal exponential second moment includes E X_i^2 = 2.
    k=[[h[min(i,j),max(i,j)]*(2 if i==j else 1) for j in range(3)] for i in range(3)]
    radial=[-2*L,L-e,2*e]
    plus_rad=sum(radial[i]*radial[j]*k[i][j] for i in range(3) for j in range(3))
    radial_fraction=((L-e)**2/q+plus_rad)/(2/q)
    internal_fraction=(4*L*L*h[0,1]+4*e*e*h[1,2])/8
    strong_fraction=(2*e/L+4*L*L*g[0]+2*e*e*g[1])/(8/L)
    weak_fraction=(2*L/e+2*L*L*g[1]+4*e*e*g[2])/(8/e)
    fractions=list(map(float,[radial_fraction,internal_fraction,strong_fraction,weak_fraction]))
    return dict(e=float(e),moment_max_residual=float(moment_residual),fractions=dict(zip(['spectral','internal','strong_null','weak_null'],fractions)),minimum=min(fractions))

if __name__=='__main__':
    data={'method':'35-digit deterministic Laplace integrals for continuous Haar readout', 'cases':[check(e) for e in ['0.5','0.1','0.01','0.001','0.00001']]}
    data['status']='pass'
    data['precision_decimal_digits']=mp.mp.dps
    data['mpmath_version']=mp.__version__
    equal=data['cases'][0]['fractions'].values()
    if max(abs(x-.25) for x in equal)>1e-14:
        raise AssertionError('Equal-spectrum class fractions must all be one quarter.')
    for row in data['cases'][1:]:
        if row['minimum'] <= .25:
            raise AssertionError('Representative near-boundary fractions must exceed one quarter.')
    if max(abs(data['cases'][-1]['fractions'][key]-.5) for key in ['spectral','internal','strong_null'])>2e-4:
        raise AssertionError('Representative near-boundary nonweak fractions.')
    if abs(data['cases'][-1]['fractions']['weak_null']-.25)>3e-5:
        raise AssertionError('Representative weak-null limit.')
    out=Path(__file__).resolve().parents[1]/'experiments/results/haar_pair.json'
    out.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))
