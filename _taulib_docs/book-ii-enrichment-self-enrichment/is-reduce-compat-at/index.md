---
{
  "projection_kind": "taulib_declaration",
  "title": "is_reduce_compat_at",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-self-enrichment/is-reduce-compat-at/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.SelfEnrichment`.",
  "declaration_id": "TauLib.BookII.Enrichment.SelfEnrichment::is_reduce_compat_at",
  "declaration_slug": "is-reduce-compat-at",
  "kind": "def",
  "name": "is_reduce_compat_at",
  "module_name": "TauLib.BookII.Enrichment.SelfEnrichment",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-self-enrichment/",
  "source_line_start": 116,
  "source_line_end": 125,
  "registry_ids": [
    "II.D54"
  ],
  "related_registry_items": [
    {
      "id": "II.D54",
      "title": "Hom Object",
      "url": "/registry/object/II.D54/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L116-L125",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.SelfEnrichment",
        "url": "/verify/taulib/docs/book-ii-enrichment-self-enrichment/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L116-L125",
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

- Module: [TauLib.BookII.Enrichment.SelfEnrichment](/verify/taulib/docs/book-ii-enrichment-self-enrichment/)
- Source path: [`TauLib/BookII/Enrichment/SelfEnrichment.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L116-L125)
- Source range: L116-L125
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D54` — Hom Object

## Immediate Comment / Docstring

```lean
/-- [II.D54] Helper: check if a map f on [0, P_k) is reduce-compatible.
    A map f is reduce-compatible at stage k if f(reduce(x, k)) = reduce(f(x), k)
    for all x in [0, P_k). For endomorphisms on Z/P_kZ, this means
    f is a well-defined endomorphism of the cyclic group. -/
```

## Source Excerpt

```lean
def is_reduce_compat_at (f : TauIdx → TauIdx) (k : TauIdx) : Bool :=
  go f k 0 (primorial k + 1)
where
  go (f : TauIdx → TauIdx) (k x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x >= primorial k then true
    else
      let ok := reduce (f x) k == f (reduce x k)
      ok && go f k (x + 1) (fuel - 1)
  termination_by fuel
```
