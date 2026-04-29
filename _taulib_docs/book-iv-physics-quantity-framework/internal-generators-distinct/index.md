---
{
  "projection_kind": "taulib_declaration",
  "title": "internal_generators_distinct",
  "permalink": "/verify/taulib/docs/book-iv-physics-quantity-framework/internal-generators-distinct/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.QuantityFramework`.",
  "declaration_id": "TauLib.BookIV.Physics.QuantityFramework::internal_generators_distinct",
  "declaration_slug": "internal-generators-distinct",
  "kind": "theorem",
  "name": "internal_generators_distinct",
  "module_name": "TauLib.BookIV.Physics.QuantityFramework",
  "module_url": "/verify/taulib/docs/book-iv-physics-quantity-framework/",
  "source_line_start": 341,
  "source_line_end": 354,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/QuantityFramework.lean#L341-L354",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.QuantityFramework",
        "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/QuantityFramework.lean#L341-L354",
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

- Module: [TauLib.BookIV.Physics.QuantityFramework](/verify/taulib/docs/book-iv-physics-quantity-framework/)
- Source path: [`TauLib/BookIV/Physics/QuantityFramework.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/QuantityFramework.lean#L341-L354)
- Source range: L341-L354
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Each internal quantity has a distinct generator. -/
```

## Source Excerpt

```lean
theorem internal_generators_distinct :
    time_internal.generator ≠ energy_internal.generator ∧
    time_internal.generator ≠ mass_internal.generator ∧
    time_internal.generator ≠ gravity_internal.generator ∧
    time_internal.generator ≠ entropy_internal.generator ∧
    energy_internal.generator ≠ mass_internal.generator ∧
    energy_internal.generator ≠ gravity_internal.generator ∧
    energy_internal.generator ≠ entropy_internal.generator ∧
    mass_internal.generator ≠ gravity_internal.generator ∧
    mass_internal.generator ≠ entropy_internal.generator ∧
    gravity_internal.generator ≠ entropy_internal.generator := by
  simp [time_internal, energy_internal, mass_internal, gravity_internal, entropy_internal]

end Tau.BookIV.Physics
```
