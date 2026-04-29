---
{
  "projection_kind": "taulib_declaration",
  "title": "all_gaps_exponential",
  "permalink": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/all-gaps-exponential/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Bridge.ConjectureGaps`.",
  "declaration_id": "TauLib.BookIII.Bridge.ConjectureGaps::all_gaps_exponential",
  "declaration_slug": "all-gaps-exponential",
  "kind": "theorem",
  "name": "all_gaps_exponential",
  "module_name": "TauLib.BookIII.Bridge.ConjectureGaps",
  "module_url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/",
  "source_line_start": 225,
  "source_line_end": 228,
  "registry_ids": [
    "III.D113"
  ],
  "related_registry_items": [
    {
      "id": "III.D113",
      "title": "Forbidden Move Mapping",
      "url": "/registry/object/III.D113/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L225-L228",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.ConjectureGaps",
        "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L225-L228",
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

- Module: [TauLib.BookIII.Bridge.ConjectureGaps](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/)
- Source path: [`TauLib/BookIII/Bridge/ConjectureGaps.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L225-L228)
- Source range: L225-L228
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D113` — Forbidden Move Mapping

## Immediate Comment / Docstring

```lean
/-- [III.D113] All three gaps map to exponential_quantification. -/
```

## Source Excerpt

```lean
theorem all_gaps_exponential :
    all_conjectures.all (fun c =>
      gap_forbidden_move c == .exponential_quantification) = true := by
  native_decide
```
