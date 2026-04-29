---
{
  "projection_kind": "taulib_declaration",
  "title": "packing_is_8_27",
  "permalink": "/verify/taulib/docs/book-v-cosmology-helium-fraction/packing-is-8-27/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.HeliumFraction`.",
  "declaration_id": "TauLib.BookV.Cosmology.HeliumFraction::packing_is_8_27",
  "declaration_slug": "packing-is-8-27",
  "kind": "theorem",
  "name": "packing_is_8_27",
  "module_name": "TauLib.BookV.Cosmology.HeliumFraction",
  "module_url": "/verify/taulib/docs/book-v-cosmology-helium-fraction/",
  "source_line_start": 90,
  "source_line_end": 92,
  "registry_ids": [
    "V.T146"
  ],
  "related_registry_items": [
    {
      "id": "V.T146",
      "title": "Packing Maximum Theorem",
      "url": "/registry/object/V.T146/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L90-L92",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.HeliumFraction",
        "url": "/verify/taulib/docs/book-v-cosmology-helium-fraction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L90-L92",
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

- Module: [TauLib.BookV.Cosmology.HeliumFraction](/verify/taulib/docs/book-v-cosmology-helium-fraction/)
- Source path: [`TauLib/BookV/Cosmology/HeliumFraction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L90-L92)
- Source range: L90-L92
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T146` — Packing Maximum Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T146] Packing is exactly 8/27. -/
```

## Source Excerpt

```lean
theorem packing_is_8_27 :
    he_packing.pack_num = 8 ∧ he_packing.pack_den = 27 :=
  ⟨rfl, rfl⟩
```
