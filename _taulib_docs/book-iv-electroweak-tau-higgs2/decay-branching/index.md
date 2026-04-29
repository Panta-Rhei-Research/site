---
{
  "projection_kind": "taulib_declaration",
  "title": "DecayBranching",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/decay-branching/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::DecayBranching",
  "declaration_slug": "decay-branching",
  "kind": "structure",
  "name": "DecayBranching",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 292,
  "source_line_end": 297,
  "registry_ids": [
    "IV.P77"
  ],
  "related_registry_items": [
    {
      "id": "IV.P77",
      "title": "Decay Mode Consistency",
      "url": "/registry/object/IV.P77/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L292-L297",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauHiggs2",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L292-L297",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs2](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L292-L297)
- Source range: L292-L297
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P77` — Decay Mode Consistency

## Immediate Comment / Docstring

```lean
/-- [IV.P77] Higgs decay branching ratios are determined by ι_τ
    through the Yukawa couplings and gauge couplings.

    Dominant channels (SM values for comparison):
    - H → bb̄: ≈ 58%
    - H → WW*: ≈ 21%
    - H → gg: ≈ 9%
    - H → ττ̄: ≈ 6%
    - H → cc̄: ≈ 3%
    - H → ZZ*: ≈ 3%

    The τ-framework predicts these from ι_τ and sector couplings
    with no free parameters. -/
```

## Source Excerpt

```lean
structure DecayBranching where
  /-- Channel label. -/
  channel : String
  /-- Branching ratio numerator (parts per 1000). -/
  br_permille : Nat
  deriving Repr
```
