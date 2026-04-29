---
{
  "projection_kind": "taulib_declaration",
  "title": "coupling_identity_at_omega",
  "permalink": "/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/coupling-identity-at-omega/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.CouplingIdentityApproximants`.",
  "declaration_id": "TauLib.BookI.Boundary.CouplingIdentityApproximants::coupling_identity_at_omega",
  "declaration_slug": "coupling-identity-at-omega",
  "kind": "theorem",
  "name": "coupling_identity_at_omega",
  "module_name": "TauLib.BookI.Boundary.CouplingIdentityApproximants",
  "module_url": "/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/",
  "source_line_start": 171,
  "source_line_end": 175,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/CouplingIdentityApproximants.lean#L171-L175",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.CouplingIdentityApproximants",
        "url": "/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/CouplingIdentityApproximants.lean#L171-L175",
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

- Module: [TauLib.BookI.Boundary.CouplingIdentityApproximants](/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/)
- Source path: [`TauLib/BookI/Boundary/CouplingIdentityApproximants.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/CouplingIdentityApproximants.lean#L171-L175)
- Source range: L171-L175
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §6.3 Theorem 6.3 `thm:coupling-identity`**:
    the coupling identity in the ω-limit:

      `ι_τ · (π_τ + e_τ) ≡ 2`   (Cauchy equivalence on TauReal)

    Equivalently, `ι_τ = 2 / (π_τ + e_τ)`.

    This is **Wave 4's operational capstone**
    `TauReal.iota_tau_mul_pi_plus_e_eq_two`, repackaged under paper
    §6.3's framing.  The paper's proof (via finite-stage
    normalisation passed through the inverse limit) and Wave 4's
    proof (via operational division + mul-inv-cancel) are two paths
    to the same conclusion; we inherit Wave 4's proof. -/
```

## Source Excerpt

```lean
theorem coupling_identity_at_omega :
    TauReal.equiv
      (TauReal.iota_tau.mul (TauReal.pi.add TauReal.e))
      TauReal.two :=
  TauReal.iota_tau_mul_pi_plus_e_eq_two
```
