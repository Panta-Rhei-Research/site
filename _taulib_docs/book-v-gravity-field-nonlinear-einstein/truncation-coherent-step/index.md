---
{
  "projection_kind": "taulib_declaration",
  "title": "TruncationCoherentStep",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/truncation-coherent-step/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.NonlinearEinstein`.",
  "declaration_id": "TauLib.BookV.GravityField.NonlinearEinstein::TruncationCoherentStep",
  "declaration_slug": "truncation-coherent-step",
  "kind": "structure",
  "name": "TruncationCoherentStep",
  "module_name": "TauLib.BookV.GravityField.NonlinearEinstein",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/",
  "source_line_start": 145,
  "source_line_end": 160,
  "registry_ids": [
    "V.D56"
  ],
  "related_registry_items": [
    {
      "id": "V.D56",
      "title": "Truncation-coherent descent",
      "url": "/registry/object/V.D56/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L145-L160",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.NonlinearEinstein",
        "url": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L145-L160",
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

- Module: [TauLib.BookV.GravityField.NonlinearEinstein](/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/)
- Source path: [`TauLib/BookV/GravityField/NonlinearEinstein.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L145-L160)
- Source range: L145-L160
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D56` — Truncation-coherent descent

## Immediate Comment / Docstring

```lean
/-- [V.D56] Truncation-coherent step: a single step in the NF
    iteration that preserves truncation coherence.

    A step from depth k to k+1 is truncation-coherent if the
    cocycle defect at k+1 is less than or equal to the defect at k.
    This ensures monotone convergence. -/
```

## Source Excerpt

```lean
structure TruncationCoherentStep where
  /-- Defect before the step. -/
  defect_before : CocycleDefect
  /-- Defect after the step. -/
  defect_after : CocycleDefect
  /-- Step number (= defect_before.step). -/
  step : Nat
  /-- Step matches before-defect step. -/
  step_match : step = defect_before.step
  /-- After step is one more than before. -/
  step_advance : defect_after.step = defect_before.step + 1
  /-- Defect decreases (cross-multiplied for Nat safety). -/
  defect_decrease :
    defect_after.defect_numer * defect_before.defect_denom ≤
    defect_before.defect_numer * defect_after.defect_denom
  deriving Repr
```
