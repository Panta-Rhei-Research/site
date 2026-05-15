---
{
  "projection_kind": "taulib_declaration",
  "title": "TauIntQ.ofInt",
  "permalink": "/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/of-int/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Bridge.TauIntQuotient`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauIntQuotient::TauIntQ.ofInt",
  "declaration_slug": "of-int",
  "kind": "def",
  "name": "TauIntQ.ofInt",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauIntQuotient",
  "module_url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/",
  "source_line_start": 280,
  "source_line_end": 282,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean#L280-L282",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Bridge.TauIntQuotient",
        "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean#L280-L282",
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

- Module: [TauLib.BookI.Boundary.Bridge.TauIntQuotient](/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/)
- Source path: [`TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean#L280-L282)
- Source range: L280-L282
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Embed `Int` into `TauIntQ` via the τ-native fromInt construction. -/
```

## Source Excerpt

```lean
def TauIntQ.ofInt (n : Int) : TauIntQ :=
  if h : n ≥ 0 then (⟨n.toNat, 0⟩ : TauInt).toQ
  else (⟨0, (-n).toNat⟩ : TauInt).toQ
```
