---
{
  "projection_kind": "taulib_declaration",
  "title": "kn_tree_numer",
  "permalink": "/verify/taulib/docs/book-v-gravity-co-rotor-coupling/kn-tree-numer/",
  "summary_short": "`def` declaration in `TauLib.BookV.Gravity.CoRotorCoupling`.",
  "declaration_id": "TauLib.BookV.Gravity.CoRotorCoupling::kn_tree_numer",
  "declaration_slug": "kn-tree-numer",
  "kind": "def",
  "name": "kn_tree_numer",
  "module_name": "TauLib.BookV.Gravity.CoRotorCoupling",
  "module_url": "/verify/taulib/docs/book-v-gravity-co-rotor-coupling/",
  "source_line_start": 154,
  "source_line_end": 154,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/CoRotorCoupling.lean#L154-L154",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.CoRotorCoupling",
        "url": "/verify/taulib/docs/book-v-gravity-co-rotor-coupling/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/CoRotorCoupling.lean#L154-L154",
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

- Module: [TauLib.BookV.Gravity.CoRotorCoupling](/verify/taulib/docs/book-v-gravity-co-rotor-coupling/)
- Source path: [`TauLib/BookV/Gravity/CoRotorCoupling.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/CoRotorCoupling.lean#L154-L154)
- Source range: L154-L154
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- κ_n^{tree} = 2√3 rational approximation.
    2√3 = 3.4641016... ≈ 2 × 17320508/10000000. -/
```

## Source Excerpt

```lean
def kn_tree_numer : Nat := 2 * sqrt3_numer  -- 34641016
```
