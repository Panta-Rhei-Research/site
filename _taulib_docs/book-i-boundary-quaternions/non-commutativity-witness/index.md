---
{
  "projection_kind": "taulib_declaration",
  "title": "non_commutativity_witness",
  "permalink": "/verify/taulib/docs/book-i-boundary-quaternions/non-commutativity-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Quaternions`.",
  "declaration_id": "TauLib.BookI.Boundary.Quaternions::non_commutativity_witness",
  "declaration_slug": "non-commutativity-witness",
  "kind": "theorem",
  "name": "non_commutativity_witness",
  "module_name": "TauLib.BookI.Boundary.Quaternions",
  "module_url": "/verify/taulib/docs/book-i-boundary-quaternions/",
  "source_line_start": 224,
  "source_line_end": 242,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Quaternions.lean#L224-L242",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Quaternions.lean#L224-L242",
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
- Source path: [`TauLib/BookI/Boundary/Quaternions.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Quaternions.lean#L224-L242)
- Source range: L224-L242
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Non-commutativity witness: qi * qj and qj * qi differ in the z-component.
    qi * qj has z = 1 while qj * qi has z = -1.

    Under the Cauchy `TauReal.equiv`, we extract the modulus, evaluate at
    tolerance level `k = 0` (bound `1/(0+1) = 1`), and derive the
    contradiction `2 < 1` from the fact that `|1 − (−1)| = 2` at every
    index of the constant z-component sequences. -/
```

## Source Excerpt

```lean
theorem non_commutativity_witness :
    ¬ TauQuaternion.equiv (TauQuaternion.mul TauQuaternion.qi TauQuaternion.qj)
                          (TauQuaternion.mul TauQuaternion.qj TauQuaternion.qi) := by
  intro ⟨_, _, _, hz⟩
  obtain ⟨μ, h⟩ := hz
  have h0 := h 0 (μ 0) (_root_.le_refl _)
  -- Unfold the Cauchy bound to an inequality in `Rat`
  unfold TauRat.lt at h0
  rw [TauRat.toRat_abs, toRat_sub, TauRat.ofNatRecip_toRat] at h0
  -- Evaluate the z-components of qi*qj and qj*qi at index `μ 0`.
  -- They are constant TauRats whose toRat values are `1` and `-1`.
  simp only [TauQuaternion.mul, TauQuaternion.qi, TauQuaternion.qj,
    TauReal.sub, TauReal.add, TauReal.mul, TauReal.negate,
    TauReal.zero, TauReal.one] at h0
  simp only [toRat_add, toRat_mul, toRat_negate, toRat_sub,
    toRat_zero, toRat_one] at h0
  -- h0 now says |(1 * 1 - 0) - (-(0 - 1 * 1))| < 1/(0+1) in Rat, i.e. |2| < 1
  push_cast at h0
  linarith [abs_nonneg ((1 : Rat) * 1 - 0 * 0 - -(0 * 0 - 1 * 1))]
```
