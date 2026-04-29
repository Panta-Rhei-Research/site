---
{
  "projection_kind": "taulib_declaration",
  "title": "germ_idempotent_supported",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/germ-idempotent-supported/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.YonedaApplied`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.YonedaApplied::germ_idempotent_supported",
  "declaration_slug": "germ-idempotent-supported",
  "kind": "theorem",
  "name": "germ_idempotent_supported",
  "module_name": "TauLib.BookII.CentralTheorem.YonedaApplied",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/",
  "source_line_start": 334,
  "source_line_end": 341,
  "registry_ids": [
    "II.T39"
  ],
  "related_registry_items": [
    {
      "id": "II.T39",
      "title": "Omega-Germs iff Holomorphic Functions",
      "url": "/registry/object/II.T39/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L334-L341",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.YonedaApplied",
        "url": "/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L334-L341",
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

- Module: [TauLib.BookII.CentralTheorem.YonedaApplied](/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/)
- Source path: [`TauLib/BookII/CentralTheorem/YonedaApplied.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L334-L341)
- Source range: L334-L341
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T39` — Omega-Germs iff Holomorphic Functions

## Immediate Comment / Docstring

```lean
/-- [II.T39] The identity omega-germ is idempotent-supported:
    e_plus * interior_bipolar(p) + e_minus * interior_bipolar(p) = interior_bipolar(p).
    This is the decompose_recovery theorem applied pointwise. -/
```

## Source Excerpt

```lean
theorem germ_idempotent_supported (p : TauAdmissiblePoint) :
    SectorPair.add
      (SectorPair.mul e_plus_sector (interior_bipolar p))
      (SectorPair.mul e_minus_sector (interior_bipolar p)) =
    interior_bipolar p := by
  simp [SectorPair.add, SectorPair.mul, e_plus_sector, e_minus_sector, interior_bipolar]

end Tau.BookII.CentralTheorem
```
