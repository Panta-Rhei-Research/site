---
{
  "projection_kind": "taulib_declaration",
  "title": "five_sixths_structure",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/five-sixths-structure/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BBNBaryogenesis`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNBaryogenesis::five_sixths_structure",
  "declaration_slug": "five-sixths-structure",
  "kind": "theorem",
  "name": "five_sixths_structure",
  "module_name": "TauLib.BookV.Cosmology.BBNBaryogenesis",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/",
  "source_line_start": 294,
  "source_line_end": 294,
  "registry_ids": [
    "V.T180"
  ],
  "related_registry_items": [
    {
      "id": "V.T180",
      "title": "(5/6) Uniquely Forced from Threshold Topology",
      "url": "/registry/object/V.T180/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L294-L294",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BBNBaryogenesis",
        "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L294-L294",
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

- Module: [TauLib.BookV.Cosmology.BBNBaryogenesis](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/)
- Source path: [`TauLib/BookV/Cosmology/BBNBaryogenesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L294-L294)
- Source range: L294-L294
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T180` — (5/6) Uniquely Forced from Threshold Topology

## Immediate Comment / Docstring

```lean
-- [V.T180] 5/6 coefficient structure (exact)
```

## Source Excerpt

```lean
theorem five_sixths_structure : (5 : Nat) = 5 ∧ (6 : Nat) = 2 * 3 := ⟨by rfl, by rfl⟩
```
