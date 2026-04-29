---
{
  "projection_kind": "taulib_declaration",
  "title": "yoneda_full_check",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/yoneda-full-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.YonedaTheorem`.",
  "declaration_id": "TauLib.BookII.Enrichment.YonedaTheorem::yoneda_full_check",
  "declaration_slug": "yoneda-full-check",
  "kind": "def",
  "name": "yoneda_full_check",
  "module_name": "TauLib.BookII.Enrichment.YonedaTheorem",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/",
  "source_line_start": 133,
  "source_line_end": 149,
  "registry_ids": [
    "II.T36"
  ],
  "related_registry_items": [
    {
      "id": "II.T36",
      "title": "Tau-Yoneda Embedding",
      "url": "/registry/object/II.T36/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L133-L149",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.YonedaTheorem",
        "url": "/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L133-L149",
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

- Module: [TauLib.BookII.Enrichment.YonedaTheorem](/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/)
- Source path: [`TauLib/BookII/Enrichment/YonedaTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L133-L149)
- Source range: L133-L149
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T36` — Tau-Yoneda Embedding

## Immediate Comment / Docstring

```lean
/-- [II.T36] Yoneda fullness: for any tower-coherent function g given
    as a restriction tower, there exists f with preyoneda(f) = g.
    The witness is f = g itself (restricted to each stage).

    Fullness check: for g(x, k) = reduce(x², k) (tower-coherent by
    mul_mod + reduction_compat), the pre-Yoneda embedding of g recovers g.
    Using the squaring function avoids the identity/mod-idempotence tautology. -/
```

## Source Excerpt

```lean
def yoneda_full_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      -- g is a tower-coherent function: g(x, k) = reduce(x², k)
      let g_xk := reduce (x * x) k
      -- Witness: f = squaring at stage k
      let f := fun n => reduce (n * n) k
      -- preyoneda(f, x, k) = f(reduce(x, k)) = reduce((reduce(x,k))², k)
      let embedded := preyoneda_embed_nat f x k
      -- This equals reduce(x², k) by Nat.mul_mod (non-trivial)
      (embedded == g_xk) && go x (k + 1) (fuel - 1)
  termination_by fuel
```
