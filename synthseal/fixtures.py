from random import Random
from .studio import Row

def adults(count:int=240,seed:int=11)->list[Row]:
    rng=Random(seed); rows=[]
    for i in range(count):
        education=rng.choices(["HS","College","Graduate"],[.45,.4,.15])[0]
        region=rng.choice(["North","South","West"])
        age=max(18,rng.gauss(40,11)); hours=max(5,rng.gauss(40,8))
        income=max(12000,18000+age*500+hours*350+{"HS":0,"College":16000,"Graduate":35000}[education]+rng.gauss(0,9000))
        target=int(income>65000)
        rows.append({"age":round(age,2),"income":round(income,2),"hours":round(hours,2),"education":education,"region":region,"target":target})
    rows[-1]={"age":91.0,"income":199000.0,"hours":77.0,"education":"Graduate","region":"Remote","target":1}
    return rows
