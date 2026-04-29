---
{
  "projection_kind": "taulib_declaration",
  "title": "characters_determined_by_pair",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/characters-determined-by-pair/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.QuantumMechanics.QuantumCharacters`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.QuantumCharacters::characters_determined_by_pair",
  "declaration_slug": "characters-determined-by-pair",
  "kind": "theorem",
  "name": "characters_determined_by_pair",
  "module_name": "TauLib.BookIV.QuantumMechanics.QuantumCharacters",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/",
  "source_line_start": 64,
  "source_line_end": 65,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L64-L65",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.QuantumCharacters",
        "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L64-L65",
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

- Module: [TauLib.BookIV.QuantumMechanics.QuantumCharacters](/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/)
- Source path: [`TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L64-L65)
- Source range: L64-L65
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Characters on T^2 are determined by exactly 2 integers. -/
```

## Source Excerpt

```lean
theorem characters_determined_by_pair :
    characters_on_torus.param_count = 2 := rfl
```
