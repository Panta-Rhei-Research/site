---
{
  "projection_kind": "taulib_declaration",
  "title": "qk_squared",
  "permalink": "/verify/taulib/docs/book-i-boundary-quaternions/qk-squared/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Quaternions`.",
  "declaration_id": "TauLib.BookI.Boundary.Quaternions::qk_squared",
  "declaration_slug": "qk-squared",
  "kind": "theorem",
  "name": "qk_squared",
  "module_name": "TauLib.BookI.Boundary.Quaternions",
  "module_url": "/verify/taulib/docs/book-i-boundary-quaternions/",
  "source_line_start": 179,
  "source_line_end": 193,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Quaternions.lean#L179-L193",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Quaternions.lean#L179-L193",
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
- Source path: [`TauLib/BookI/Boundary/Quaternions.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Quaternions.lean#L179-L193)
- Source range: L179-L193
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- k^2 = -1: qk * qk is equivalent to negate one. -/
```

## Source Excerpt

```lean
theorem qk_squared :
    TauQuaternion.equiv (TauQuaternion.mul TauQuaternion.qk TauQuaternion.qk)
                        TauQuaternion.neg_one := by
  refine ⟨TauReal.equiv_of_pointwise ?_, TauReal.equiv_of_pointwise ?_,
          TauReal.equiv_of_pointwise ?_, TauReal.equiv_of_pointwise ?_⟩ <;>
    intro n <;>
  simp only [TauQuaternion.mul, TauQuaternion.qk, TauQuaternion.neg_one,
    TauQuaternion.negate, TauQuaternion.one,
    TauReal.sub, TauReal.add, TauReal.mul, TauReal.negate,
    TauReal.zero, TauReal.one,
    TauRat.equiv, TauRat.sub, TauRat.add, TauRat.mul, TauRat.negate,
    TauRat.zero, TauRat.one] <;>
  rw [equiv_iff_toInt_eq] <;>
  simp only [toInt_add, toInt_mul, toInt_negate, toInt_fromNat, toInt_zero, toInt_one] <;>
  push_cast <;> ring
```
