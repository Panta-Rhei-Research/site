---
{
  "projection_kind": "taulib_declaration",
  "title": "ns_eos_from_defect",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-compact-objects/ns-eos-from-defect/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.CompactObjects`.",
  "declaration_id": "TauLib.BookV.Astrophysics.CompactObjects::ns_eos_from_defect",
  "declaration_slug": "ns-eos-from-defect",
  "kind": "theorem",
  "name": "ns_eos_from_defect",
  "module_name": "TauLib.BookV.Astrophysics.CompactObjects",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/",
  "source_line_start": 125,
  "source_line_end": 127,
  "registry_ids": [
    "V.P71"
  ],
  "related_registry_items": [
    {
      "id": "V.P71",
      "title": "Neutron Star EOS Structure --- V.P35",
      "url": "/registry/object/V.P71/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/CompactObjects.lean#L125-L127",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.CompactObjects",
        "url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/CompactObjects.lean#L125-L127",
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

- Module: [TauLib.BookV.Astrophysics.CompactObjects](/verify/taulib/docs/book-v-astrophysics-compact-objects/)
- Source path: [`TauLib/BookV/Astrophysics/CompactObjects.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/CompactObjects.lean#L125-L127)
- Source range: L125-L127
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P71` — Neutron Star EOS Structure --- V.P35

## Immediate Comment / Docstring

```lean
/-- [V.P71] Neutron star EOS from defect bundle: the equation of
    state of neutron-star matter is determined by the defect-bundle
    structure at nuclear densities.

    At density ρ > ρ_nuclear, the defect tuple's compression
    component dominates, stiffening the EOS and setting the
    TOV maximum mass. -/
```

## Source Excerpt

```lean
theorem ns_eos_from_defect :
    "NS EOS = defect-bundle compression component at nuclear density" =
    "NS EOS = defect-bundle compression component at nuclear density" := rfl
```
