---
{
  "projection_kind": "taulib_declaration",
  "title": "identity_decoder",
  "permalink": "/verify/taulib/docs/book-iii-computation-e2-agent/identity-decoder/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Computation.E2Agent`.",
  "declaration_id": "TauLib.BookIII.Computation.E2Agent::identity_decoder",
  "declaration_slug": "identity-decoder",
  "kind": "theorem",
  "name": "identity_decoder",
  "module_name": "TauLib.BookIII.Computation.E2Agent",
  "module_url": "/verify/taulib/docs/book-iii-computation-e2-agent/",
  "source_line_start": 176,
  "source_line_end": 179,
  "registry_ids": [
    "III.D50"
  ],
  "related_registry_items": [
    {
      "id": "III.D50",
      "title": "Operational Closure",
      "url": "/registry/object/III.D50/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Agent.lean#L176-L179",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Agent.lean#L176-L179",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookIII/Computation/E2Agent.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Agent.lean#L176-L179)
- Source range: L176-L179
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D50` — Operational Closure

## Immediate Comment / Docstring

```lean
/-- [III.D50] Structural: identity decoder (d=0) is a fixpoint. -/
```

## Source Excerpt

```lean
theorem identity_decoder :
    agent_step ⟨7, 0, 3⟩ = 7 := by native_decide

end Tau.BookIII.Computation
```
