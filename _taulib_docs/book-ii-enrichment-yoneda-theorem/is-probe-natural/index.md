---
{
  "projection_kind": "taulib_declaration",
  "title": "is_probe_natural",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/is-probe-natural/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.YonedaTheorem`.",
  "declaration_id": "TauLib.BookII.Enrichment.YonedaTheorem::is_probe_natural",
  "declaration_slug": "is-probe-natural",
  "kind": "def",
  "name": "is_probe_natural",
  "module_name": "TauLib.BookII.Enrichment.YonedaTheorem",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/",
  "source_line_start": 52,
  "source_line_end": 53,
  "registry_ids": [
    "II.L11"
  ],
  "related_registry_items": [
    {
      "id": "II.L11",
      "title": "Probe Naturality iff Yoneda",
      "url": "/registry/object/II.L11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L52-L53",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L52-L53",
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
- Source path: [`TauLib/BookII/Enrichment/YonedaTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L52-L53)
- Source range: L52-L53
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.L11` — Probe Naturality iff Yoneda

## Immediate Comment / Docstring

```lean
/-- [II.L11] Probe naturality for a Nat-valued function:
    reduce(f(reduce(x, k+1)), k) = f(reduce(x, k)).
    This is the explicit form of naturality with respect to
    the restriction maps in the primorial inverse system. -/
```

## Source Excerpt

```lean
def is_probe_natural (f : TauIdx → TauIdx) (x k : TauIdx) : Bool :=
  reduce (f (reduce x (k + 1))) k == f (reduce x k)
```
