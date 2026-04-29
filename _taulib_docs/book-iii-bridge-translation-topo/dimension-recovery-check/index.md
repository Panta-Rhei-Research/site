---
{
  "projection_kind": "taulib_declaration",
  "title": "dimension_recovery_check",
  "permalink": "/verify/taulib/docs/book-iii-bridge-translation-topo/dimension-recovery-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.TranslationTopo`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationTopo::dimension_recovery_check",
  "declaration_slug": "dimension-recovery-check",
  "kind": "def",
  "name": "dimension_recovery_check",
  "module_name": "TauLib.BookIII.Bridge.TranslationTopo",
  "module_url": "/verify/taulib/docs/book-iii-bridge-translation-topo/",
  "source_line_start": 89,
  "source_line_end": 110,
  "registry_ids": [
    "III.D90"
  ],
  "related_registry_items": [
    {
      "id": "III.D90",
      "title": "Dimension Recovery",
      "url": "/registry/object/III.D90/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L89-L110",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.TranslationTopo",
        "url": "/verify/taulib/docs/book-iii-bridge-translation-topo/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L89-L110",
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

- Module: [TauLib.BookIII.Bridge.TranslationTopo](/verify/taulib/docs/book-iii-bridge-translation-topo/)
- Source path: [`TauLib/BookIII/Bridge/TranslationTopo.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L89-L110)
- Source range: L89-L110
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D90` — Dimension Recovery

## Immediate Comment / Docstring

```lean
/-- [III.D90] Dimension recovery check: the number of independent
    prime coordinates equals the stage depth. -/
```

## Source Excerpt

```lean
def dimension_recovery_check (db : Nat) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      -- Count distinct prime factors of M_k
      let pk := primorial k
      let dim := count_prime_factors pk k
      (dim == k) && go (k + 1) (fuel - 1)
  termination_by fuel
  count_prime_factors (pk k : Nat) : Nat :=
    go_count 1 (k + 1) pk 0
  termination_by 0
  go_count (i bound pk acc : Nat) : Nat :=
    if i > bound then acc
    else
      let p := nth_prime i
      let has_factor := p > 0 && pk % p == 0
      go_count (i + 1) bound pk (acc + if has_factor then 1 else 0)
  termination_by bound + 1 - i
```
