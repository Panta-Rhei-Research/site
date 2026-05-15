---
{
  "projection_kind": "taulib_declaration",
  "title": "b_only_fun",
  "permalink": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/b-only-fun/",
  "summary_short": "`def` declaration in `TauLib.BookI.Holomorphy.DHolomorphic`.",
  "declaration_id": "TauLib.BookI.Holomorphy.DHolomorphic::b_only_fun",
  "declaration_slug": "b-only-fun",
  "kind": "def",
  "name": "b_only_fun",
  "module_name": "TauLib.BookI.Holomorphy.DHolomorphic",
  "module_url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/",
  "source_line_start": 140,
  "source_line_end": 140,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DHolomorphic.lean#L140-L140",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.DHolomorphic",
        "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DHolomorphic.lean#L140-L140",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookI.Holomorphy.DHolomorphic](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/)
- Source path: [`TauLib/BookI/Holomorphy/DHolomorphic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DHolomorphic.lean#L140-L140)
- Source range: L140-L140
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A sector function that is zero on the C-sector: f(u,v) = (g(u), 0).
    This is D-holomorphic but has no C-sector information. -/
```

## Source Excerpt

```lean
def b_only_fun (g : Int → Int) : SectorFun := ⟨g, fun _ => 0⟩
```
