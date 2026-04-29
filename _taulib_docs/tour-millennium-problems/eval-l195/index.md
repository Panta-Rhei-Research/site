---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L195",
  "permalink": "/verify/taulib/docs/tour-millennium-problems/eval-l195/",
  "summary_short": "`eval` declaration in `TauLib.Tour.MillenniumProblems`.",
  "declaration_id": "TauLib.Tour.MillenniumProblems::#eval:195",
  "declaration_slug": "eval-l195",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.Tour.MillenniumProblems",
  "module_url": "/verify/taulib/docs/tour-millennium-problems/",
  "source_line_start": 195,
  "source_line_end": 226,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/MillenniumProblems.lean#L195-L226",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.Tour.MillenniumProblems",
        "url": "/verify/taulib/docs/tour-millennium-problems/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/MillenniumProblems.lean#L195-L226",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.Tour.MillenniumProblems](/verify/taulib/docs/tour-millennium-problems/)
- Source path: [`TauLib/Tour/MillenniumProblems.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/MillenniumProblems.lean#L195-L226)
- Source range: L195-L226
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- 8 bridge entries, classified by scope:
```

## Source Excerpt

```lean
#eval bridge_ledger_len  -- 8

-- Scope counts:
-- 1 established (Poincaré — already proved by Perelman)
-- 1 bridge break (P vs NP — recognized as outside τ's scope)
-- 6 conjectural (require infinite extensions of finite checks)

-- The ledger's own consistency is a theorem:
#check bridge_ledger_consistent
  -- : bridge_ledger_check = true   (by native_decide)

-- Honest claims: every established/τ-effective claim passes its check:
#check honest_claim_8_3

/-
This is the standard: if we claim it, you can check it.
If it requires an infinite extension, we mark it as conjectural
and show you the finite check that passes.

No hand-waving. No hidden assumptions. Scope labels on every claim.


WHAT COMES NEXT

• BookIII/Doors/GrandGRH.lean               — Full GRH reformulation
• BookIII/Doors/SpectralCorrespondence.lean  — O3 spectral bridge
• BookIII/Arithmetic/BSD.lean                — BSD three-ingredient proof
• BookIII/Doors/Poincaré.lean                — Gluing guarantee
• BookIII/Bridge/BridgeAxiom.lean            — The scope ledger
• BookIII/Spectral/AdditiveConjectures.lean  — Goldbach, twin primes
• BookIII/Spectral/TwinPrimeDeep.lean        — Deep twin prime analysis
-/
```
