---
{
  "projection_kind": "taulib_declaration",
  "title": "primorial_base_diverges",
  "permalink": "/verify/taulib/docs/book-ii-interior-omega-readout/primorial-base-diverges/",
  "summary_short": "`def` declaration in `TauLib.BookII.Interior.OmegaReadout`.",
  "declaration_id": "TauLib.BookII.Interior.OmegaReadout::primorial_base_diverges",
  "declaration_slug": "primorial-base-diverges",
  "kind": "def",
  "name": "primorial_base_diverges",
  "module_name": "TauLib.BookII.Interior.OmegaReadout",
  "module_url": "/verify/taulib/docs/book-ii-interior-omega-readout/",
  "source_line_start": 85,
  "source_line_end": 92,
  "registry_ids": [
    "II.T02"
  ],
  "related_registry_items": [
    {
      "id": "II.T02",
      "title": "Fiber Degeneration at Omega",
      "url": "/registry/object/II.T02/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/OmegaReadout.lean#L85-L92",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Interior.OmegaReadout",
        "url": "/verify/taulib/docs/book-ii-interior-omega-readout/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/OmegaReadout.lean#L85-L92",
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

- Module: [TauLib.BookII.Interior.OmegaReadout](/verify/taulib/docs/book-ii-interior-omega-readout/)
- Source path: [`TauLib/BookII/Interior/OmegaReadout.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/OmegaReadout.lean#L85-L92)
- Source range: L85-L92
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T02` — Fiber Degeneration at Omega

## Immediate Comment / Docstring

```lean
/-- [II.T02] Primorial base readout: A-values exhaust primes. -/
```

## Source Excerpt

```lean
def primorial_base_diverges : Bool :=
  let as := primorial_witness.map fun (_, p) => p.a
  -- A-values strictly increasing
  go as
where
  go : List TauIdx → Bool
    | [] | [_] => true
    | x :: y :: rest => x < y && go (y :: rest)
```
