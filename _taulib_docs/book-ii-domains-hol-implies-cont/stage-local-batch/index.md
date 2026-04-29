---
{
  "projection_kind": "taulib_declaration",
  "title": "stage_local_batch",
  "permalink": "/verify/taulib/docs/book-ii-domains-hol-implies-cont/stage-local-batch/",
  "summary_short": "`def` declaration in `TauLib.BookII.Domains.HolImpliesCont`.",
  "declaration_id": "TauLib.BookII.Domains.HolImpliesCont::stage_local_batch",
  "declaration_slug": "stage-local-batch",
  "kind": "def",
  "name": "stage_local_batch",
  "module_name": "TauLib.BookII.Domains.HolImpliesCont",
  "module_url": "/verify/taulib/docs/book-ii-domains-hol-implies-cont/",
  "source_line_start": 54,
  "source_line_end": 61,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/HolImpliesCont.lean#L54-L61",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Domains.HolImpliesCont",
        "url": "/verify/taulib/docs/book-ii-domains-hol-implies-cont/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/HolImpliesCont.lean#L54-L61",
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

- Module: [TauLib.BookII.Domains.HolImpliesCont](/verify/taulib/docs/book-ii-domains-hol-implies-cont/)
- Source path: [`TauLib/BookII/Domains/HolImpliesCont.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/HolImpliesCont.lean#L54-L61)
- Source range: L54-L61
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Batch stage locality across stages 1..k_max. -/
```

## Source Excerpt

```lean
def stage_local_batch (sf : StageFun) (k_max bound : TauIdx) : Bool :=
  go 1 (k_max + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > k_max then true
    else stage_local_check sf k bound && go (k + 1) (fuel - 1)
  termination_by fuel
```
