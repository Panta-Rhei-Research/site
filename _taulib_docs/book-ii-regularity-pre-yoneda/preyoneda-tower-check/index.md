---
{
  "projection_kind": "taulib_declaration",
  "title": "preyoneda_tower_check",
  "permalink": "/verify/taulib/docs/book-ii-regularity-pre-yoneda/preyoneda-tower-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.PreYoneda`.",
  "declaration_id": "TauLib.BookII.Regularity.PreYoneda::preyoneda_tower_check",
  "declaration_slug": "preyoneda-tower-check",
  "kind": "def",
  "name": "preyoneda_tower_check",
  "module_name": "TauLib.BookII.Regularity.PreYoneda",
  "module_url": "/verify/taulib/docs/book-ii-regularity-pre-yoneda/",
  "source_line_start": 80,
  "source_line_end": 96,
  "registry_ids": [
    "II.D50"
  ],
  "related_registry_items": [
    {
      "id": "II.D50",
      "title": "Pre-Yoneda Embedding",
      "url": "/registry/object/II.D50/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L80-L96",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.PreYoneda",
        "url": "/verify/taulib/docs/book-ii-regularity-pre-yoneda/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L80-L96",
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

- Module: [TauLib.BookII.Regularity.PreYoneda](/verify/taulib/docs/book-ii-regularity-pre-yoneda/)
- Source path: [`TauLib/BookII/Regularity/PreYoneda.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L80-L96)
- Source range: L80-L96
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D50` — Pre-Yoneda Embedding

## Immediate Comment / Docstring

```lean
/-- [II.D50] Tower coherence check for the pre-Yoneda embedding:
    verify that for a reduce-based function f,
    reduce(preyoneda(f, x, k+1), k) = preyoneda(f, x, k).

    A reduce-based function satisfies f(reduce(x, k)) = reduce(f(x), k).
    For such f, the pre-Yoneda embedding is tower-coherent:
      reduce(f(reduce(x, k+1)), k) = f(reduce(reduce(x, k+1), k))
                                    = f(reduce(x, k))

    We test with f = reduce(_, stage) for various stages. -/
```

## Source Excerpt

```lean
def preyoneda_tower_check (bound db : TauIdx) : Bool :=
  go 2 1 (bound * db + bound + db + 1)
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k >= db then go (x + 1) 1 (fuel - 1)
    else
      -- Test function: f(n) = reduce(n, k+1) composed with stage reduction
      -- preyoneda(id, x, k) = reduce(x, k)
      -- preyoneda(id, x, k+1) = reduce(x, k+1)
      -- reduce(preyoneda(id, x, k+1), k) = reduce(reduce(x, k+1), k) = reduce(x, k)
      let embed_k := reduce x k
      let embed_k1 := reduce x (k + 1)
      let reduced := reduce embed_k1 k
      (reduced == embed_k) && go x (k + 1) (fuel - 1)
  termination_by fuel
```
