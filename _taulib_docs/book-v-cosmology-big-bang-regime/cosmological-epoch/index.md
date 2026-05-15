---
{
  "projection_kind": "taulib_declaration",
  "title": "CosmologicalEpoch",
  "permalink": "/corpus/taulib/docs/book-v-cosmology-big-bang-regime/cosmological-epoch/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Cosmology.BigBangRegime`.",
  "declaration_id": "TauLib.BookV.Cosmology.BigBangRegime::CosmologicalEpoch",
  "declaration_slug": "cosmological-epoch",
  "kind": "inductive",
  "name": "CosmologicalEpoch",
  "module_name": "TauLib.BookV.Cosmology.BigBangRegime",
  "module_url": "/corpus/taulib/docs/book-v-cosmology-big-bang-regime/",
  "source_line_start": 93,
  "source_line_end": 100,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BigBangRegime.lean#L93-L100",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BigBangRegime",
        "url": "/corpus/taulib/docs/book-v-cosmology-big-bang-regime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BigBangRegime.lean#L93-L100",
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

- Module: [TauLib.BookV.Cosmology.BigBangRegime](/corpus/taulib/docs/book-v-cosmology-big-bang-regime/)
- Source path: [`TauLib/BookV/Cosmology/BigBangRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BigBangRegime.lean#L93-L100)
- Source range: L93-L100
- Kind: `inductive`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Cosmological epoch classification within the τ-framework. -/
```

## Source Excerpt

```lean
inductive CosmologicalEpoch where
  /-- Pre-hadronic: α₁ to neutron threshold. -/
  | PreHadronic
  /-- Hadronic: neutron threshold to nucleosynthesis. -/
  | Hadronic
  /-- Present: post-nucleosynthesis. -/
  | Present
  deriving Repr, DecidableEq, BEq
```
