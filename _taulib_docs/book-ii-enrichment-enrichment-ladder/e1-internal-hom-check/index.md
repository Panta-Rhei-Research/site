---
{
  "projection_kind": "taulib_declaration",
  "title": "e1_internal_hom_check",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/e1-internal-hom-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.EnrichmentLadder`.",
  "declaration_id": "TauLib.BookII.Enrichment.EnrichmentLadder::e1_internal_hom_check",
  "declaration_slug": "e1-internal-hom-check",
  "kind": "def",
  "name": "e1_internal_hom_check",
  "module_name": "TauLib.BookII.Enrichment.EnrichmentLadder",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/",
  "source_line_start": 155,
  "source_line_end": 180,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L155-L180",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.EnrichmentLadder",
        "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L155-L180",
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

- Module: [TauLib.BookII.Enrichment.EnrichmentLadder](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/)
- Source path: [`TauLib/BookII/Enrichment/EnrichmentLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L155-L180)
- Source range: L155-L180
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.D58, E1 clause] E1 internal hom check:
    verify that the hom-count at stage k projects correctly to stage k-1.
    That is, every reduce-compatible map at stage k restricts to a
    reduce-compatible map at stage k-1.

    Concretely: if f : Z/P_kZ -> Z/P_kZ is reduce-compatible, then
    the restriction f|_{Z/P_{k-1}Z} defined by
      f_restricted(x) = reduce(f(x), k-1)
    is a reduce-compatible map on Z/P_{k-1}Z.

    This is the KEY E1 property: Hom_k -> Hom_{k-1} is well-defined,
    making the hom counts into a tower (an internal tau-object). -/
```

## Source Excerpt

```lean
def e1_internal_hom_check (db : TauIdx) : Bool :=
  go 2 (db * 10 + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      -- The identity map at stage k: id_k(x) = reduce(x, k)
      -- Its restriction to stage k-1: reduce(id_k(x), k-1) = reduce(reduce(x, k), k-1)
      --   = reduce(x, k-1) = id_{k-1}(x)
      -- So id_k restricts to id_{k-1}. Tower-compatible.
      let id_ok := check_id_restriction k 0 20 (fuel - 1)
      -- The constant-zero map at stage k: zero_k(x) = 0
      -- Restriction: reduce(0, k-1) = 0 = zero_{k-1}(x). Tower-compatible.
      let zero_ok := reduce 0 (k - 1) == 0
      id_ok && zero_ok && go (k + 1) (fuel - 1)
  termination_by fuel
  check_id_restriction (k x bound fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k = 0 then true
    else
      let restricted := reduce (reduce x k) (k - 1)
      let direct := reduce x (k - 1)
      (restricted == direct) && check_id_restriction k (x + 1) bound (fuel - 1)
  termination_by fuel
```
