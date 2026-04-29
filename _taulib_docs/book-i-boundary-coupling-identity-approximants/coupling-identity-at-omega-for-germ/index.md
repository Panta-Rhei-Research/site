---
{
  "projection_kind": "taulib_declaration",
  "title": "coupling_identity_at_omega_for_germ",
  "permalink": "/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/coupling-identity-at-omega-for-germ/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.CouplingIdentityApproximants`.",
  "declaration_id": "TauLib.BookI.Boundary.CouplingIdentityApproximants::coupling_identity_at_omega_for_germ",
  "declaration_slug": "coupling-identity-at-omega-for-germ",
  "kind": "theorem",
  "name": "coupling_identity_at_omega_for_germ",
  "module_name": "TauLib.BookI.Boundary.CouplingIdentityApproximants",
  "module_url": "/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/",
  "source_line_start": 287,
  "source_line_end": 290,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/CouplingIdentityApproximants.lean#L287-L290",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/CouplingIdentityApproximants.lean#L287-L290",
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
- Source path: [`TauLib/BookI/Boundary/CouplingIdentityApproximants.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/CouplingIdentityApproximants.lean#L287-L290)
- Source range: L287-L290
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Bridge to Wave 11's zero-arg coupling_identity**: the paper
    §6.3 coupling identity transfers to *every* crossing-point
    defect germ via Wave 11's `coupling_identity`.

    For any `g : CrossingPointDefectGerm` with `IsCrossingPoint g`,
    `Read g · (π + e) ≡ 2` holds at Cauchy equivalence; this is
    Wave 11's form of paper §6.3. -/
```

## Source Excerpt

```lean
theorem coupling_identity_at_omega_for_germ
    (g : CrossingPointDefectGerm) (h : IsCrossingPoint g) :
    TauReal.equiv ((Read g).mul (TauReal.pi.add TauReal.e)) TauReal.two :=
  coupling_identity g h
```
