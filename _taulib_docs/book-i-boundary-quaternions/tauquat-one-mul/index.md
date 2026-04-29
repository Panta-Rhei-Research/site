---
{
  "projection_kind": "taulib_declaration",
  "title": "tauquat_one_mul",
  "permalink": "/verify/taulib/docs/book-i-boundary-quaternions/tauquat-one-mul/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Quaternions`.",
  "declaration_id": "TauLib.BookI.Boundary.Quaternions::tauquat_one_mul",
  "declaration_slug": "tauquat-one-mul",
  "kind": "theorem",
  "name": "tauquat_one_mul",
  "module_name": "TauLib.BookI.Boundary.Quaternions",
  "module_url": "/verify/taulib/docs/book-i-boundary-quaternions/",
  "source_line_start": 293,
  "source_line_end": 321,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Quaternions.lean#L293-L321",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Quaternions.lean#L293-L321",
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
- Source path: [`TauLib/BookI/Boundary/Quaternions.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Quaternions.lean#L293-L321)
- Source range: L293-L321
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- One is a left identity for quaternion multiplication (up to equiv). -/
```

## Source Excerpt

```lean
theorem tauquat_one_mul (a : TauQuaternion) :
    TauQuaternion.equiv (TauQuaternion.mul TauQuaternion.one a) a := by
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

-- ============================================================
-- SMOKE TESTS
-- ============================================================

#check TauQuaternion.mul TauQuaternion.qi TauQuaternion.qj
#check qi_squared
#check qj_squared
#check qk_squared
#check ijk_relation
#check non_commutativity_witness
#check tauquat_add_comm
#check tauquat_mul_one
#check tauquat_one_mul

end Tau.Boundary
```
