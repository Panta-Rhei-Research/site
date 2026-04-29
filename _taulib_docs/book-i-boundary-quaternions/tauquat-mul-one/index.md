---
{
  "projection_kind": "taulib_declaration",
  "title": "tauquat_mul_one",
  "permalink": "/verify/taulib/docs/book-i-boundary-quaternions/tauquat-mul-one/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Quaternions`.",
  "declaration_id": "TauLib.BookI.Boundary.Quaternions::tauquat_mul_one",
  "declaration_slug": "tauquat-mul-one",
  "kind": "theorem",
  "name": "tauquat_mul_one",
  "module_name": "TauLib.BookI.Boundary.Quaternions",
  "module_url": "/verify/taulib/docs/book-i-boundary-quaternions/",
  "source_line_start": 278,
  "source_line_end": 290,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Quaternions.lean#L278-L290",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Quaternions",
        "url": "/verify/taulib/docs/book-i-boundary-quaternions/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Quaternions.lean#L278-L290",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookI.Boundary.Quaternions](/verify/taulib/docs/book-i-boundary-quaternions/)
- Source path: [`TauLib/BookI/Boundary/Quaternions.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Quaternions.lean#L278-L290)
- Source range: L278-L290
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- One is a right identity for quaternion multiplication (up to equiv). -/
```

## Source Excerpt

```lean
theorem tauquat_mul_one (a : TauQuaternion) :
    TauQuaternion.equiv (TauQuaternion.mul a TauQuaternion.one) a := by
  refine ⟨TauReal.equiv_of_pointwise ?_, TauReal.equiv_of_pointwise ?_,
          TauReal.equiv_of_pointwise ?_, TauReal.equiv_of_pointwise ?_⟩ <;>
    intro n <;>
  simp only [TauQuaternion.mul, TauQuaternion.one,
    TauReal.sub, TauReal.add, TauReal.mul, TauReal.negate,
    TauReal.zero, TauReal.one,
    TauRat.equiv, TauRat.sub, TauRat.add, TauRat.mul, TauRat.negate,
    TauRat.zero, TauRat.one] <;>
  rw [equiv_iff_toInt_eq] <;>
  simp only [toInt_add, toInt_mul, toInt_negate, toInt_fromNat, toInt_zero, toInt_one] <;>
  push_cast <;> ring
```
