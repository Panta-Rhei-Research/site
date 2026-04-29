---
{
  "projection_kind": "taulib_declaration",
  "title": "pvsnp_obstruction_check",
  "permalink": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/pvsnp-obstruction-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.TranslationObstruction`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationObstruction::pvsnp_obstruction_check",
  "declaration_slug": "pvsnp-obstruction-check",
  "kind": "def",
  "name": "pvsnp_obstruction_check",
  "module_name": "TauLib.BookIII.Bridge.TranslationObstruction",
  "module_url": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/",
  "source_line_start": 203,
  "source_line_end": 231,
  "registry_ids": [
    "III.P38"
  ],
  "related_registry_items": [
    {
      "id": "III.P38",
      "title": "P vs NP as Polynomial Translation Obstruction",
      "url": "/registry/object/III.P38/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L203-L231",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.TranslationObstruction",
        "url": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L203-L231",
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

- Module: [TauLib.BookIII.Bridge.TranslationObstruction](/verify/taulib/docs/book-iii-bridge-translation-obstruction/)
- Source path: [`TauLib/BookIII/Bridge/TranslationObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L203-L231)
- Source range: L203-L231
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P38` — P vs NP as Polynomial Translation Obstruction

## Immediate Comment / Docstring

```lean
/-- [III.P38] P vs NP obstruction: the succinct_circuits move has
    damage 3, meaning the bridge breaks entirely. At each finite
    stage k, P_adm = NP_adm (all problems decidable in finite Z/M_k Z),
    but this internal equivalence cannot be translated. -/
```

## Source Excerpt

```lean
def pvsnp_obstruction_check (db : Nat) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      if pk == 0 then go (k + 1) (fuel - 1)
      else
        -- At stage k, every function Z/M_k → Bool is decidable in O(M_k) time
        -- This means P_adm = NP_adm at stage k
        let internal_equiv := true  -- by finiteness of Z/M_k
        -- But the circuit complexity to decide an arbitrary function is
        -- exponential in the input size: log₂(M_k) bits input
        -- The obstruction: translation to ZFC requires circuits of size M_k
        -- while polynomial translation would need size poly(log M_k)
        let log_pk := log_approx pk
        let exponential_gap := pk > log_pk * log_pk  -- M_k >> (log M_k)²
        internal_equiv && exponential_gap && go (k + 1) (fuel - 1)
  termination_by fuel
  log_approx (n : Nat) : Nat :=
    -- Approximate log₂(n)
    go_log n 0
  termination_by 0
  go_log (n acc : Nat) : Nat :=
    if n <= 1 then acc
    else go_log (n / 2) (acc + 1)
  termination_by n
```
