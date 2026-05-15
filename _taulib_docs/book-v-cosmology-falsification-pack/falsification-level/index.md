---
{
  "projection_kind": "taulib_declaration",
  "title": "FalsificationLevel",
  "permalink": "/corpus/taulib/docs/book-v-cosmology-falsification-pack/falsification-level/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Cosmology.FalsificationPack`.",
  "declaration_id": "TauLib.BookV.Cosmology.FalsificationPack::FalsificationLevel",
  "declaration_slug": "falsification-level",
  "kind": "inductive",
  "name": "FalsificationLevel",
  "module_name": "TauLib.BookV.Cosmology.FalsificationPack",
  "module_url": "/corpus/taulib/docs/book-v-cosmology-falsification-pack/",
  "source_line_start": 57,
  "source_line_end": 64,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L57-L64",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.FalsificationPack",
        "url": "/corpus/taulib/docs/book-v-cosmology-falsification-pack/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L57-L64",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookV.Cosmology.FalsificationPack](/corpus/taulib/docs/book-v-cosmology-falsification-pack/)
- Source path: [`TauLib/BookV/Cosmology/FalsificationPack.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L57-L64)
- Source range: L57-L64
- Kind: `inductive`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Falsification level classification. -/
```

## Source Excerpt

```lean
inductive FalsificationLevel where
  /-- Level 1: structural (refutes framework). -/
  | Structural
  /-- Level 2: quantitative (tests specific numbers). -/
  | Quantitative
  /-- Level 3: observational frontier (needs future tech). -/
  | ObservationalFrontier
  deriving Repr, DecidableEq, BEq
```
