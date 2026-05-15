---
{
  "projection_kind": "taulib_declaration",
  "title": "circuits_break_bridge",
  "permalink": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/circuits-break-bridge/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Bridge.ForbiddenMoves`.",
  "declaration_id": "TauLib.BookIII.Bridge.ForbiddenMoves::circuits_break_bridge",
  "declaration_slug": "circuits-break-bridge",
  "kind": "theorem",
  "name": "circuits_break_bridge",
  "module_name": "TauLib.BookIII.Bridge.ForbiddenMoves",
  "module_url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/",
  "source_line_start": 264,
  "source_line_end": 265,
  "registry_ids": [
    "III.T43"
  ],
  "related_registry_items": [
    {
      "id": "III.T43",
      "title": "Move-Bridge Correspondence",
      "url": "/registry/object/III.T43/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L264-L265",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.ForbiddenMoves",
        "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L264-L265",
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

- Module: [TauLib.BookIII.Bridge.ForbiddenMoves](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/)
- Source path: [`TauLib/BookIII/Bridge/ForbiddenMoves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L264-L265)
- Source range: L264-L265
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.T43` — Move-Bridge Correspondence

## Immediate Comment / Docstring

```lean
/-- [III.T43] Structural: succinct circuits cause bridge break. -/
```

## Source Excerpt

```lean
theorem circuits_break_bridge :
    bridge_damage .succinct_circuits = 3 := rfl
```
