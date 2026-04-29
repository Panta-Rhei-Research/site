---
{
  "projection_kind": "taulib_declaration",
  "title": "YangMillsMassGap",
  "permalink": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/yang-mills-mass-gap/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.YangMillsGap`.",
  "declaration_id": "TauLib.BookIV.Strong.YangMillsGap::YangMillsMassGap",
  "declaration_slug": "yang-mills-mass-gap",
  "kind": "structure",
  "name": "YangMillsMassGap",
  "module_name": "TauLib.BookIV.Strong.YangMillsGap",
  "module_url": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/",
  "source_line_start": 310,
  "source_line_end": 321,
  "registry_ids": [
    "IV.T75"
  ],
  "related_registry_items": [
    {
      "id": "IV.T75",
      "title": "τ-Yang--Mills Mass Gap Theorem",
      "url": "/registry/object/IV.T75/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L310-L321",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.YangMillsGap",
        "url": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L310-L321",
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

- Module: [TauLib.BookIV.Strong.YangMillsGap](/verify/taulib/docs/book-iv-strong-yang-mills-gap/)
- Source path: [`TauLib/BookIV/Strong/YangMillsGap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L310-L321)
- Source range: L310-L321
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T75` — τ-Yang--Mills Mass Gap Theorem

## Immediate Comment / Docstring

```lean
/-- [IV.T75] The tau-Yang-Mills Mass Gap Theorem:
    In the C-sector at E1 level:
    1. The strong vacuum Gamma_s^*[omega] has a positive spectral gap
       delta_infinity^s > 0.
    2. The gap mode g[omega] exists.
    3. The gap is non-perturbative (not accessible by perturbation
       theory around the vacuum).

    Proof structure:
    - Step 1: Gap positivity at each finite stage (IV.P107)
    - Step 2: Tower monotonicity (IV.P108)
    - Step 3: Profinite spectral preservation (IV.T74)
    - Step 4: Gap Meta-Theorem (IV.T73) applies

    Scope: tau-effective (proved within the tau-framework). -/
```

## Source Excerpt

```lean
structure YangMillsMassGap where
  /-- Spectral gap is positive at omega. -/
  gap_positive : Bool := true
  /-- Gap mode exists. -/
  gap_mode_exists : Bool := true
  /-- Gap is non-perturbative. -/
  non_perturbative : Bool := true
  /-- Scope: tau-effective. -/
  scope : String := "tau-effective"
  /-- Four proof steps. -/
  step_count : Nat := 4
  deriving Repr
```
