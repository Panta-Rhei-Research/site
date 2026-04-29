---
{
  "projection_kind": "taulib_declaration",
  "title": "coupling_identity_via_bounded_mul",
  "permalink": "/verify/taulib/docs/book-i-boundary-iota-tau-structural/coupling-identity-via-bounded-mul/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.IotaTauStructural`.",
  "declaration_id": "TauLib.BookI.Boundary.IotaTauStructural::coupling_identity_via_bounded_mul",
  "declaration_slug": "coupling-identity-via-bounded-mul",
  "kind": "theorem",
  "name": "coupling_identity_via_bounded_mul",
  "module_name": "TauLib.BookI.Boundary.IotaTauStructural",
  "module_url": "/verify/taulib/docs/book-i-boundary-iota-tau-structural/",
  "source_line_start": 219,
  "source_line_end": 227,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/IotaTauStructural.lean#L219-L227",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.IotaTauStructural",
        "url": "/verify/taulib/docs/book-i-boundary-iota-tau-structural/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/IotaTauStructural.lean#L219-L227",
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

- Module: [TauLib.BookI.Boundary.IotaTauStructural](/verify/taulib/docs/book-i-boundary-iota-tau-structural/)
- Source path: [`TauLib/BookI/Boundary/IotaTauStructural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/IotaTauStructural.lean#L219-L227)
- Source range: L219-L227
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Coupling identity, refined form** — uses the Wave 2.5
    `mul_respects_equiv_right_of_bound` directly, leaving only the
    `(π + e)`-bound as a parameter (a Nat M plus the per-index bound
    `∀ n, |(π+e).approx n| ≤ M`).  The Wave 2.5 mul-congruence
    bridge is now internal to the proof; the *only* remaining
    parameter is the explicit bound on `(π + e)`.

    Once a concrete `(π + e).bound_le_seven` lemma is added to
    `TauRealPiPlusE.lean` (a small follow-up using the Wave 3
    monotonicity infrastructure), the bound and its proof can be
    supplied automatically and a fully zero-arg `coupling_identity`
    becomes statable. -/
```

## Source Excerpt

```lean
theorem coupling_identity_via_bounded_mul
    (g : CrossingPointDefectGerm) (h : IsCrossingPoint g)
    (M : Nat) (hM : 1 ≤ M)
    (h_bound : ∀ n, ((TauReal.pi.add TauReal.e).approx n).abs.toRat ≤ M) :
    TauReal.equiv ((Read g).mul (TauReal.pi.add TauReal.e)) TauReal.two := by
  have h_read := iota_tau_read_eq_division g h
  have h_mul_equiv := TauReal.mul_respects_equiv_right_of_bound
    (Read g) TauReal.iota_tau (TauReal.pi.add TauReal.e) M hM h_bound h_read
  exact TauReal.equiv_trans h_mul_equiv TauReal.iota_tau_mul_pi_plus_e_eq_two
```
