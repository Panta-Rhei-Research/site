---
{
  "projection_kind": "taulib_declaration",
  "title": "universe_rank",
  "permalink": "/corpus/taulib/docs/book-iii-bridge-zfcas-vm/universe-rank/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.ZFCasVM`.",
  "declaration_id": "TauLib.BookIII.Bridge.ZFCasVM::universe_rank",
  "declaration_slug": "universe-rank",
  "kind": "def",
  "name": "universe_rank",
  "module_name": "TauLib.BookIII.Bridge.ZFCasVM",
  "module_url": "/corpus/taulib/docs/book-iii-bridge-zfcas-vm/",
  "source_line_start": 194,
  "source_line_end": 194,
  "registry_ids": [
    "III.D70"
  ],
  "related_registry_items": [
    {
      "id": "III.D70",
      "title": "Host-Level Property",
      "url": "/registry/object/III.D70/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L194-L194",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.ZFCasVM",
        "url": "/corpus/taulib/docs/book-iii-bridge-zfcas-vm/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L194-L194",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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

- Module: [TauLib.BookIII.Bridge.ZFCasVM](/corpus/taulib/docs/book-iii-bridge-zfcas-vm/)
- Source path: [`TauLib/BookIII/Bridge/ZFCasVM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L194-L194)
- Source range: L194-L194
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- `III.D70` — Host-Level Property

## Immediate Comment / Docstring

```lean
/-- [III.D70] Cumulative hierarchy V_k: sets of rank <= k are
    tau-addresses x < Prim(k). The universe grows strictly with k. -/
```

## Source Excerpt

```lean
def universe_rank (k : TauIdx) : TauIdx := primorial k
```
