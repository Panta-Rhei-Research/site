---
{
  "projection_kind": "taulib_declaration",
  "title": "one_axiom",
  "permalink": "/corpus/taulib/docs/book-iii-bridge-bridge-axiom/one-axiom/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Bridge.BridgeAxiom`.",
  "declaration_id": "TauLib.BookIII.Bridge.BridgeAxiom::one_axiom",
  "declaration_slug": "one-axiom",
  "kind": "theorem",
  "name": "one_axiom",
  "module_name": "TauLib.BookIII.Bridge.BridgeAxiom",
  "module_url": "/corpus/taulib/docs/book-iii-bridge-bridge-axiom/",
  "source_line_start": 372,
  "source_line_end": 372,
  "registry_ids": [
    "III.D71"
  ],
  "related_registry_items": [
    {
      "id": "III.D71",
      "title": "Bridge Axiom",
      "url": "/registry/object/III.D71/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L372-L372",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.BridgeAxiom",
        "url": "/corpus/taulib/docs/book-iii-bridge-bridge-axiom/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L372-L372",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIII.Bridge.BridgeAxiom](/corpus/taulib/docs/book-iii-bridge-bridge-axiom/)
- Source path: [`TauLib/BookIII/Bridge/BridgeAxiom.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L372-L372)
- Source range: L372-L372
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.D71` — Bridge Axiom

## Immediate Comment / Docstring

```lean
/-- [III.D71] Structural: bridge axiom is the ONLY conjectural postulate. -/
```

## Source Excerpt

```lean
theorem one_axiom : rh_conjectural_layer = 3 := rfl
```
