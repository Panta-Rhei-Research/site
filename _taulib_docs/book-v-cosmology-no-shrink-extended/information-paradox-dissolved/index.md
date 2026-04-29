---
{
  "projection_kind": "taulib_declaration",
  "title": "information_paradox_dissolved",
  "permalink": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/information-paradox-dissolved/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.NoShrinkExtended`.",
  "declaration_id": "TauLib.BookV.Cosmology.NoShrinkExtended::information_paradox_dissolved",
  "declaration_slug": "information-paradox-dissolved",
  "kind": "def",
  "name": "information_paradox_dissolved",
  "module_name": "TauLib.BookV.Cosmology.NoShrinkExtended",
  "module_url": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/",
  "source_line_start": 174,
  "source_line_end": 176,
  "registry_ids": [
    "V.R226"
  ],
  "related_registry_items": [
    {
      "id": "V.R226",
      "title": "Information Paradox Dissolved",
      "url": "/registry/object/V.R226/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L174-L176",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.NoShrinkExtended",
        "url": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L174-L176",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookV.Cosmology.NoShrinkExtended](/verify/taulib/docs/book-v-cosmology-no-shrink-extended/)
- Source path: [`TauLib/BookV/Cosmology/NoShrinkExtended.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L174-L176)
- Source range: L174-L176
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.R226` — Information Paradox Dissolved

## Immediate Comment / Docstring

```lean
/-- [V.R226] Information paradox dissolved: the paradox dissolves
    because assumption (1) — that BHs evaporate — is false.

    No information-losing process occurs. Unitarity is preserved
    trivially because the ontic state never loses information. -/
```

## Source Excerpt

```lean
def information_paradox_dissolved : Prop :=
  "BHs don't evaporate => no information loss => no paradox" =
  "BHs don't evaporate => no information loss => no paradox"
```
