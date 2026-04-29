---
{
  "projection_kind": "taulib_declaration",
  "title": "boundary_coherence_check",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-homological/boundary-coherence-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.Homological`.",
  "declaration_id": "TauLib.BookII.Enrichment.Homological::boundary_coherence_check",
  "declaration_slug": "boundary-coherence-check",
  "kind": "def",
  "name": "boundary_coherence_check",
  "module_name": "TauLib.BookII.Enrichment.Homological",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-homological/",
  "source_line_start": 60,
  "source_line_end": 75,
  "registry_ids": [
    "II.D84"
  ],
  "related_registry_items": [
    {
      "id": "II.D84",
      "title": "Chain Complex",
      "url": "/registry/object/II.D84/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L60-L75",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.Homological",
        "url": "/verify/taulib/docs/book-ii-enrichment-homological/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L60-L75",
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

- Module: [TauLib.BookII.Enrichment.Homological](/verify/taulib/docs/book-ii-enrichment-homological/)
- Source path: [`TauLib/BookII/Enrichment/Homological.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L60-L75)
- Source range: L60-L75
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D84` — Chain Complex

## Immediate Comment / Docstring

```lean
/-- [II.D84] Tower coherence: d_{n-1} ∘ d_n = d_{n-1} (reduction composes).
    reduce(reduce(x, n-1), n-2) = reduce(x, n-2) for n ≥ 2. -/
```

## Source Excerpt

```lean
def boundary_coherence_check (k : Nat) : Bool :=
  go 2 0 k (k * (primorial k + 1))
where
  go (n x maxk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if n > maxk then true
    else if x >= primorial n then go (n + 1) 0 maxk (fuel - 1)
    else
      let d1 := primorial_chain.boundary n x
      let d2 := primorial_chain.boundary (n - 1) d1
      -- Tower coherence: reduce(reduce(x, n-1), n-2) = reduce(x, n-2)
      let dd_ok := if n >= 2 then
        d2 == primorial_chain.boundary (n - 1) x
      else true
      dd_ok && go n (x + 1) maxk (fuel - 1)
  termination_by fuel
```
