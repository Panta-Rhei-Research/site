---
{
  "projection_kind": "taulib_declaration",
  "title": "E2Agent",
  "permalink": "/verify/taulib/docs/book-iii-computation-e2-agent/e2-agent/",
  "summary_short": "`structure` declaration in `TauLib.BookIII.Computation.E2Agent`.",
  "declaration_id": "TauLib.BookIII.Computation.E2Agent::E2Agent",
  "declaration_slug": "e2-agent",
  "kind": "structure",
  "name": "E2Agent",
  "module_name": "TauLib.BookIII.Computation.E2Agent",
  "module_url": "/verify/taulib/docs/book-iii-computation-e2-agent/",
  "source_line_start": 37,
  "source_line_end": 41,
  "registry_ids": [
    "III.D49"
  ],
  "related_registry_items": [
    {
      "id": "III.D49",
      "title": "E₂ Computational Agent",
      "url": "/registry/object/III.D49/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Agent.lean#L37-L41",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.E2Agent",
        "url": "/verify/taulib/docs/book-iii-computation-e2-agent/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Agent.lean#L37-L41",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookIII.Computation.E2Agent](/verify/taulib/docs/book-iii-computation-e2-agent/)
- Source path: [`TauLib/BookIII/Computation/E2Agent.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Agent.lean#L37-L41)
- Source range: L37-L41
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `III.D49` — E₂ Computational Agent

## Immediate Comment / Docstring

```lean
/-- [III.D49] E₂ agent: code + decoder pair. Both are τ-addresses at
    some primorial depth. The decoder transforms codes into new codes. -/
```

## Source Excerpt

```lean
structure E2Agent where
  code : TauIdx         -- the program-as-τ-address
  decoder : TauIdx      -- the decoder-as-τ-address
  depth : TauIdx        -- primorial depth of operation
  deriving Repr, DecidableEq, BEq
```
