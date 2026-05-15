---
{
  "projection_kind": "taulib_declaration",
  "title": "fanout_violates_K3",
  "permalink": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/fanout-violates-k3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Bridge.ForbiddenMoves`.",
  "declaration_id": "TauLib.BookIII.Bridge.ForbiddenMoves::fanout_violates_K3",
  "declaration_slug": "fanout-violates-k3",
  "kind": "theorem",
  "name": "fanout_violates_K3",
  "module_name": "TauLib.BookIII.Bridge.ForbiddenMoves",
  "module_url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/",
  "source_line_start": 256,
  "source_line_end": 257,
  "registry_ids": [
    "III.D69"
  ],
  "related_registry_items": [
    {
      "id": "III.D69",
      "title": "Five Forbidden Moves",
      "url": "/registry/object/III.D69/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L256-L257",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L256-L257",
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
- Source path: [`TauLib/BookIII/Bridge/ForbiddenMoves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L256-L257)
- Source range: L256-L257
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.D69` — Five Forbidden Moves

## Immediate Comment / Docstring

```lean
/-- [III.D69] Structural: unbounded fanout violates K3 (boundary). -/
```

## Source Excerpt

```lean
theorem fanout_violates_K3 :
    violated_axiom .unbounded_fanout = .K3 := rfl
```
