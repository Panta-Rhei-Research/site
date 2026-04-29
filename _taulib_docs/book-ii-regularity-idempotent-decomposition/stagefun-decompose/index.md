---
{
  "projection_kind": "taulib_declaration",
  "title": "stagefun_decompose",
  "permalink": "/verify/taulib/docs/book-ii-regularity-idempotent-decomposition/stagefun-decompose/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.IdempotentDecomposition`.",
  "declaration_id": "TauLib.BookII.Regularity.IdempotentDecomposition::stagefun_decompose",
  "declaration_slug": "stagefun-decompose",
  "kind": "def",
  "name": "stagefun_decompose",
  "module_name": "TauLib.BookII.Regularity.IdempotentDecomposition",
  "module_url": "/verify/taulib/docs/book-ii-regularity-idempotent-decomposition/",
  "source_line_start": 157,
  "source_line_end": 162,
  "registry_ids": [
    "II.D48"
  ],
  "related_registry_items": [
    {
      "id": "II.D48",
      "title": "Canonical Decomposition",
      "url": "/registry/object/II.D48/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L157-L162",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.IdempotentDecomposition",
        "url": "/verify/taulib/docs/book-ii-regularity-idempotent-decomposition/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L157-L162",
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

- Module: [TauLib.BookII.Regularity.IdempotentDecomposition](/verify/taulib/docs/book-ii-regularity-idempotent-decomposition/)
- Source path: [`TauLib/BookII/Regularity/IdempotentDecomposition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L157-L162)
- Source range: L157-L162
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D48` — Canonical Decomposition

## Immediate Comment / Docstring

```lean
/-- [II.D48] Decompose a StageFun into its B-channel and C-channel
    components. The B-channel component has c_fun = 0, the C-channel
    component has b_fun = 0.

    This is the stagewise lift of the idempotent decomposition. -/
```

## Source Excerpt

```lean
def stagefun_decompose (sf : StageFun) : StageFun × StageFun :=
  -- B-channel: keep b_fun, zero out c_fun
  let b_part : StageFun := ⟨sf.b_fun, fun _ _ => 0⟩
  -- C-channel: zero out b_fun, keep c_fun
  let c_part : StageFun := ⟨fun _ _ => 0, sf.c_fun⟩
  (b_part, c_part)
```
