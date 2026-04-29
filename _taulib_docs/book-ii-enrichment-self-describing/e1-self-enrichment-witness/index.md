---
{
  "projection_kind": "taulib_declaration",
  "title": "e1_self_enrichment_witness",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-self-describing/e1-self-enrichment-witness/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.SelfDescribing`.",
  "declaration_id": "TauLib.BookII.Enrichment.SelfDescribing::e1_self_enrichment_witness",
  "declaration_slug": "e1-self-enrichment-witness",
  "kind": "def",
  "name": "e1_self_enrichment_witness",
  "module_name": "TauLib.BookII.Enrichment.SelfDescribing",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-self-describing/",
  "source_line_start": 66,
  "source_line_end": 93,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L66-L93",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.SelfDescribing",
        "url": "/verify/taulib/docs/book-ii-enrichment-self-describing/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L66-L93",
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

- Module: [TauLib.BookII.Enrichment.SelfDescribing](/verify/taulib/docs/book-ii-enrichment-self-describing/)
- Source path: [`TauLib/BookII/Enrichment/SelfDescribing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L66-L93)
- Source range: L66-L93
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.D57, clause 1] Self-enrichment witness:
    for each stage k in [1, db], verify that at least one
    reduce-compatible endomorphism exists (the identity map and
    constant maps are always reduce-compatible).

    The identity map: reduce(reduce(x, k), k-1) = reduce(x, k-1)
    follows from reduction_compat. This makes Hom(A,A) nonempty
    at every stage, so Hom objects are genuine tau-objects. -/
```

## Source Excerpt

```lean
def e1_self_enrichment_witness (bound db : TauIdx) : Bool :=
  go 1 (bound * db + bound + db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let id_ok := check_id k 0 bound (fuel - 1)
      let const_ok := check_const k 0 bound (fuel - 1)
      id_ok && const_ok && go (k + 1) (fuel - 1)
  termination_by fuel
  check_id (k x bound fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k = 0 then true
    else
      let val_at_k := reduce x k
      let reduced_val := reduce val_at_k (k - 1)
      let val_at_km1 := reduce x (k - 1)
      (reduced_val == val_at_km1) && check_id k (x + 1) bound (fuel - 1)
  termination_by fuel
  check_const (k x bound fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k = 0 then true
    else
      (reduce 0 (k - 1) == 0) && check_const k (x + 1) bound (fuel - 1)
  termination_by fuel
```
