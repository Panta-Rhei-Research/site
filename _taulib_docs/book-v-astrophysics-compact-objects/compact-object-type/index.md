---
{
  "projection_kind": "taulib_declaration",
  "title": "CompactObjectType",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-compact-objects/compact-object-type/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Astrophysics.CompactObjects`.",
  "declaration_id": "TauLib.BookV.Astrophysics.CompactObjects::CompactObjectType",
  "declaration_slug": "compact-object-type",
  "kind": "inductive",
  "name": "CompactObjectType",
  "module_name": "TauLib.BookV.Astrophysics.CompactObjects",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/",
  "source_line_start": 66,
  "source_line_end": 75,
  "registry_ids": [
    "V.D124"
  ],
  "related_registry_items": [
    {
      "id": "V.D124",
      "title": "Degeneracy Pressure Character --- V.D57",
      "url": "/registry/object/V.D124/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/CompactObjects.lean#L66-L75",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/CompactObjects.lean#L66-L75",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
      "status": "defined"
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
- Source path: [`TauLib/BookV/Astrophysics/CompactObjects.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/CompactObjects.lean#L66-L75)
- Source range: L66-L75
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `V.D124` — Degeneracy Pressure Character --- V.D57

## Immediate Comment / Docstring

```lean
/-- [V.D124] Compact object type classification by defect-bundle
    topology and degeneracy boundary. -/
```

## Source Excerpt

```lean
inductive CompactObjectType where
  /-- White dwarf: electron degeneracy, S² topology. -/
  | WhiteDwarf
  /-- Neutron star: neutron degeneracy, S² topology. -/
  | NeutronStar
  /-- Black hole: torus vacuum, T² topology. -/
  | BlackHole
  /-- Hypothetical quark star (not yet confirmed). -/
  | QuarkStar
  deriving Repr, DecidableEq, BEq
```
