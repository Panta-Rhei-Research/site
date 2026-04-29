---
{
  "projection_kind": "taulib_declaration",
  "title": "yoneda_roundtrip_check",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/yoneda-roundtrip-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.YonedaTheorem`.",
  "declaration_id": "TauLib.BookII.Enrichment.YonedaTheorem::yoneda_roundtrip_check",
  "declaration_slug": "yoneda-roundtrip-check",
  "kind": "def",
  "name": "yoneda_roundtrip_check",
  "module_name": "TauLib.BookII.Enrichment.YonedaTheorem",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/",
  "source_line_start": 213,
  "source_line_end": 229,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L213-L229",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L213-L229",
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
- Source path: [`TauLib/BookII/Enrichment/YonedaTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L213-L229)
- Source range: L213-L229
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T36` — Tau-Yoneda Embedding

## Immediate Comment / Docstring

```lean
/-- [II.T36] Yoneda round-trip via Code/Decode:
    Decode(Code(preyoneda(f))) = preyoneda(f).
    This combines II.T35 (Code/Decode bijection) with II.D50 (pre-Yoneda). -/
```

## Source Excerpt

```lean
def yoneda_roundtrip_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let f := fun n => reduce n k
      -- preyoneda value at (x, k)
      let embedded := (preyoneda_embed_nat f x k : Int)
      -- Code the embedding
      let coded : TauIdx → Int := fun a => (preyoneda_embed_nat f a k : Int)
      -- Decode back
      let decoded := decode_reconstruct coded k x
      (decoded == embedded) && go x (k + 1) (fuel - 1)
  termination_by fuel
```
