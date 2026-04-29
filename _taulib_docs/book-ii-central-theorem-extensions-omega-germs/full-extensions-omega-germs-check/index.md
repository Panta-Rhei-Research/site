---
{
  "projection_kind": "taulib_declaration",
  "title": "full_extensions_omega_germs_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/full-extensions-omega-germs-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms::full_extensions_omega_germs_check",
  "declaration_slug": "full-extensions-omega-germs-check",
  "kind": "def",
  "name": "full_extensions_omega_germs_check",
  "module_name": "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/",
  "source_line_start": 274,
  "source_line_end": 281,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L274-L281",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms",
        "url": "/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L274-L281",
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

- Module: [TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms](/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/)
- Source path: [`TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L274-L281)
- Source range: L274-L281
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.L13 + II.T38] Complete verification:
    - Stagewise naturality (II.L13)
    - Strong naturality (II.L13)
    - Multi-step naturality (II.L13)
    - Omega-germ transformer (II.T38)
    - BndLift StageFun coherence (II.T38)
    - Extension-germ roundtrip (II.T38)
    - Extension sector roundtrip (II.T38) -/
```

## Source Excerpt

```lean
def full_extensions_omega_germs_check (bound db : TauIdx) : Bool :=
  stagewise_naturality_check bound db &&
  stagewise_naturality_strong_check bound db &&
  stagewise_naturality_multi_check bound db &&
  omega_germ_transformer_check bound db &&
  bndlift_stagefun_coherent_check bound db &&
  extension_germ_roundtrip_check bound db &&
  extension_sector_roundtrip_check bound db
```
