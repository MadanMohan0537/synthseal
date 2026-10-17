import argparse,csv,json
from pathlib import Path
from .fixtures import adults
from .studio import evaluate_release,generate,rare_disclosure_audit,remove_exposed

def main()->None:
    p=argparse.ArgumentParser(); p.add_argument("--output",type=Path,default=Path("release")); args=p.parse_args(); args.output.mkdir(parents=True,exist_ok=True)
    data=adults(); train=data[:179]+[data[-1]]; test=data[179:239]
    base=generate(train,180); challenged=base+[dict(train[-1])]
    before=evaluate_release(train,test,challenged); findings=rare_disclosure_audit(train,challenged)
    cleaned=remove_exposed(challenged,findings); after=evaluate_release(train,test,cleaned)
    with (args.output/"synthetic.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(cleaned[0])); w.writeheader(); w.writerows(cleaned)
    report={"product":"SynthSeal","before_remediation":before,"after_remediation":after}
    (args.output/"report.json").write_text(json.dumps(report,indent=2)+"\n")
    card=f"""# SynthSeal data card

- Source: deterministic Adult-shaped synthetic fixture; no real people.
- Purpose: demonstrate utility/privacy release evidence.
- Rows released: {len(cleaned)}
- TSTR utility gap: {after['utility_gap']:.3f}
- Membership attack rate: {after['membership_attack_rate']:.3f}
- Rare-record exposures: {before['rare_exposures']} before, {after['rare_exposures']} after remediation.
- Not approved for decisions about people or as evidence of formal privacy.
"""
    (args.output/"DATA_CARD.md").write_text(card)
    print(json.dumps({"released_rows":len(cleaned),"rare_exposures_before":before["rare_exposures"],"rare_exposures_after":after["rare_exposures"],"utility_gap_after":after["utility_gap"]},indent=2))
if __name__=="__main__": main()
