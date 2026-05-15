---
{
  "projection_kind": "taulib_declaration",
  "title": "pred_lrd_sharp_transition",
  "permalink": "/corpus/taulib/docs/book-v-cosmology-falsification-pack/pred-lrd-sharp-transition/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.FalsificationPack`.",
  "declaration_id": "TauLib.BookV.Cosmology.FalsificationPack::pred_lrd_sharp_transition",
  "declaration_slug": "pred-lrd-sharp-transition",
  "kind": "def",
  "name": "pred_lrd_sharp_transition",
  "module_name": "TauLib.BookV.Cosmology.FalsificationPack",
  "module_url": "/corpus/taulib/docs/book-v-cosmology-falsification-pack/",
  "source_line_start": 237,
  "source_line_end": 262,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L237-L262",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.FalsificationPack",
        "url": "/corpus/taulib/docs/book-v-cosmology-falsification-pack/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L237-L262",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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

- Module: [TauLib.BookV.Cosmology.FalsificationPack](/corpus/taulib/docs/book-v-cosmology-falsification-pack/)
- Source path: [`TauLib/BookV/Cosmology/FalsificationPack.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L237-L262)
- Source range: L237-L262
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Q7 (N15.D): V.T-LRD-1D sharp slope transition at upper cutoff. -/
```

## Source Excerpt

```lean
def pred_lrd_sharp_transition : TestablePrediction where
  name := "Q7 (N15.D): LRD upper-cutoff sharp slope transition"
  level := .Quantitative
  description :=
    "V.T-LRD-1D: slope transition from 0+-0.3 to <= -2 at" ++
    " upper cutoff. The original v2.1 Hossenfelder ask was" ++
    " <= 0.2 dex single-edge. Wave R7 specialist outputs gave" ++
    " incompatible widths (Specialist A: 1.66 dex outer-cutoff" ++
    " binary mechanism; Specialist C: 0.41 dex unit-Jacobian" ++
    " smooth-fraction mechanism); Wave R7 Specialist F's" ++
    " reconciliation (Inayoshi-Mayer-Bonoli-Haiman lens) found" ++
    " both mechanisms genuinely apply in different sub-regions," ++
    " with composite width 0.9^{+0.5}_{-0.4} dex (68% CI)." ++
    " v2.2 (acknowledged in v2.3 §7 Gap 7) shipped the relaxed" ++
    " <= 1.5 dex composite operational falsifier; Wave R10-4" ++
    " resynced the HeavySeedBirth.lean carrier" ++
    " (transition_width_x100 = 150, invariant <= 150). See" ++
    " research-notes/V-T-LRD-1-derivation.md §5."
  status :=
    "Operational falsifier (<= 1.5 dex composite) is now" ++
    " well-defined in v2.2/v2.3 and the Lean carrier (Wave" ++
    " R10-4). Currently_testable left false here pending a" ++
    " separate downstream review of testability gating against" ++
    " the JWST cycle 4-5 LRD sample (out of scope for the" ++
    " R10-4 carrier-resync sprint)."
  currently_testable := false
```
