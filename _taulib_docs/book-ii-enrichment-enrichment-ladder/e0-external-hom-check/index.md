---
{
  "projection_kind": "taulib_declaration",
  "title": "e0_external_hom_check",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/e0-external-hom-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.EnrichmentLadder`.",
  "declaration_id": "TauLib.BookII.Enrichment.EnrichmentLadder::e0_external_hom_check",
  "declaration_slug": "e0-external-hom-check",
  "kind": "def",
  "name": "e0_external_hom_check",
  "module_name": "TauLib.BookII.Enrichment.EnrichmentLadder",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/",
  "source_line_start": 96,
  "source_line_end": 107,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L96-L107",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L96-L107",
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
- Source path: [`TauLib/BookII/Enrichment/EnrichmentLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L96-L107)
- Source range: L96-L107
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.D58, E0 clause] E0 external hom check:
    at each stage k, verify that at least two reduce-compatible
    endomorphisms exist (the identity map and constant-zero map).

    At k=1 (P_1=2): maps {0,1} -> {0,1} that are reduce-compatible with
    stage 0 (P_0=1). Since reduce(x, 0) = x % 1 = 0 for all x, the
    compatibility condition reduce(f(x), 0) = f(reduce(x, 0)) becomes
    0 = f(0) % 1 = 0, which is always true. All 4 maps work.

    At k=2 (P_2=6): maps Z/6Z -> Z/6Z compatible with stage 1.
    The identity map and constant maps are always compatible. -/
```

## Source Excerpt

```lean
def e0_external_hom_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      let id_ok := e0_check_id_compat k 0 (pk + 1)
      let zero_ok := e0_check_zero_compat k
      id_ok && zero_ok && go (k + 1) (fuel - 1)
  termination_by fuel
```
