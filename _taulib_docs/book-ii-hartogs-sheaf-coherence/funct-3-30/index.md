---
{
  "projection_kind": "taulib_declaration",
  "title": "funct_3_30",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/funct-3-30/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Hartogs.SheafCoherence`.",
  "declaration_id": "TauLib.BookII.Hartogs.SheafCoherence::funct_3_30",
  "declaration_slug": "funct-3-30",
  "kind": "theorem",
  "name": "funct_3_30",
  "module_name": "TauLib.BookII.Hartogs.SheafCoherence",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/",
  "source_line_start": 486,
  "source_line_end": 487,
  "registry_ids": [
    "II.D47"
  ],
  "related_registry_items": [
    {
      "id": "II.D47",
      "title": "Holomorphic Presheaf",
      "url": "/registry/object/II.D47/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L486-L487",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.SheafCoherence",
        "url": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L486-L487",
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

- Module: [TauLib.BookII.Hartogs.SheafCoherence](/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/)
- Source path: [`TauLib/BookII/Hartogs/SheafCoherence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L486-L487)
- Source range: L486-L487
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.D47` — Holomorphic Presheaf

## Immediate Comment / Docstring

```lean
-- Functoriality [II.D47]
```

## Source Excerpt

```lean
theorem funct_3_30 :
    functoriality_check 3 30 = true := by native_decide
```
