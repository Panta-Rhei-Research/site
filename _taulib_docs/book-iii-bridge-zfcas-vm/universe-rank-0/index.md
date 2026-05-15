---
{
  "projection_kind": "taulib_declaration",
  "title": "universe_rank_0",
  "permalink": "/corpus/taulib/docs/book-iii-bridge-zfcas-vm/universe-rank-0/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Bridge.ZFCasVM`.",
  "declaration_id": "TauLib.BookIII.Bridge.ZFCasVM::universe_rank_0",
  "declaration_slug": "universe-rank-0",
  "kind": "theorem",
  "name": "universe_rank_0",
  "module_name": "TauLib.BookIII.Bridge.ZFCasVM",
  "module_url": "/corpus/taulib/docs/book-iii-bridge-zfcas-vm/",
  "source_line_start": 295,
  "source_line_end": 295,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L295-L295",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L295-L295",
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

- Module: [TauLib.BookIII.Bridge.ZFCasVM](/corpus/taulib/docs/book-iii-bridge-zfcas-vm/)
- Source path: [`TauLib/BookIII/Bridge/ZFCasVM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L295-L295)
- Source range: L295-L295
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.D70` — Host-Level Property

## Immediate Comment / Docstring

```lean
/-- [III.D70] Structural: V_0 = Prim(0) = 1 (singleton universe). -/
```

## Source Excerpt

```lean
theorem universe_rank_0 : universe_rank 0 = 1 := by native_decide
```
