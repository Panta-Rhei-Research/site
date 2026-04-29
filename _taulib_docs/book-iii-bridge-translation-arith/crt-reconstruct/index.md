---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_reconstruct",
  "permalink": "/verify/taulib/docs/book-iii-bridge-translation-arith/crt-reconstruct/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.TranslationArith`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationArith::crt_reconstruct",
  "declaration_slug": "crt-reconstruct",
  "kind": "def",
  "name": "crt_reconstruct",
  "module_name": "TauLib.BookIII.Bridge.TranslationArith",
  "module_url": "/verify/taulib/docs/book-iii-bridge-translation-arith/",
  "source_line_start": 102,
  "source_line_end": 112,
  "registry_ids": [
    "III.D88"
  ],
  "related_registry_items": [
    {
      "id": "III.D88",
      "title": "CRT-Integer Correspondence",
      "url": "/registry/object/III.D88/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationArith.lean#L102-L112",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.TranslationArith",
        "url": "/verify/taulib/docs/book-iii-bridge-translation-arith/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationArith.lean#L102-L112",
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

- Module: [TauLib.BookIII.Bridge.TranslationArith](/verify/taulib/docs/book-iii-bridge-translation-arith/)
- Source path: [`TauLib/BookIII/Bridge/TranslationArith.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationArith.lean#L102-L112)
- Source range: L102-L112
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D88` — CRT-Integer Correspondence

## Immediate Comment / Docstring

```lean
/-- [III.D88] CRT reconstruction: find the unique y in [0, M_k) with the
    same residues as x. (This IS x mod M_k by CRT.) -/
```

## Source Excerpt

```lean
def crt_reconstruct (x k : Nat) : Nat :=
  let pk := primorial k
  if pk == 0 then 0
  else
    go 0 pk x k
where
  go (y pk x k : Nat) : Nat :=
    if y >= pk then 0  -- fallback
    else if crt_residues_match x y k then y
    else go (y + 1) pk x k
  termination_by pk - y
```
